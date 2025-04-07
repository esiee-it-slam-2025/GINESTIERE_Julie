import { CartItem, DBError, ICartDatabase } from '@/src/interfaces/IndexedDB';

// Database configuration
const DB_NAME = 'EventCartDB';
const DB_VERSION = 1;
const CART_STORE = 'cartItems';

/**
 * CartDatabase class
 * Implements the ICartDatabase interface to provide
 * access to the IndexedDB storage for cart items
 */
class CartDatabase implements ICartDatabase {
  private db: IDBDatabase | null = null;
  private isInitialized: boolean = false;
  
  /**
   * Initialize the database
   * @returns {Promise<void>} - Resolves when DB is ready
   */
  async init(): Promise<void> {
    if (this.isInitialized) return Promise.resolve();
    
    return new Promise<void>((resolve, reject) => {
      // Check if IndexedDB is supported
      if (!window.indexedDB) {
        const error = "Your browser doesn't support IndexedDB. Please upgrade to a modern browser.";
        console.error(error);
        return reject(new Error(error));
      }
      
      const request = indexedDB.open(DB_NAME, DB_VERSION);
      
      // Handle database upgrades/creation
      request.onupgradeneeded = (event: IDBVersionChangeEvent) => {
        const db = (event.target as IDBOpenDBRequest).result;
        
        // Create the cart items object store with auto-incrementing ID
        if (!db.objectStoreNames.contains(CART_STORE)) {
          const objectStore = db.createObjectStore(CART_STORE, { 
            keyPath: 'id', 
            autoIncrement: true 
          });
          
          // Create indexes for efficient queries
          objectStore.createIndex('eventId', 'eventId', { unique: false });
          objectStore.createIndex('category', 'category', { unique: false });
          
          console.log('Cart database created successfully');
        }
      };
      
      // Handle successful database open
      request.onsuccess = (event: Event) => {
        this.db = (event.target as IDBOpenDBRequest).result;
        this.isInitialized = true;
        console.log('Cart database opened successfully');
        resolve();
      };
      
      // Handle errors
      request.onerror = (event: Event) => {
        const error = (event.target as IDBOpenDBRequest).error;
        console.error('IndexedDB error:', error);
        reject(error || new Error('Failed to open cart database'));
      };
    });
  }
  
  /**
   * Add an item to the cart
   * @param {number} eventId - The event ID (integer)
   * @param {string} category - The category (string)
   * @returns {Promise<number>} - Resolves with the ID of the new item
   */
  async addToCart(eventId: number, category: string): Promise<number> {
    await this.init();
    
    // Validate inputs
    if (!Number.isInteger(eventId)) {
      throw new Error('Event ID must be an integer');
    }
    
    if (typeof category !== 'string' || !category.trim()) {
      throw new Error('Category must be a non-empty string');
    }
    
    const cartItem: CartItem = {
      eventId: eventId,
      category: category.trim(),
      addedAt: new Date().toISOString()
    };
    
    return new Promise<number>((resolve, reject) => {
      if (!this.db) {
        return reject(new Error('Database not initialized'));
      }
      
      const transaction = this.db.transaction([CART_STORE], 'readwrite');
      const store = transaction.objectStore(CART_STORE);
      
      const request = store.add(cartItem);
      
      request.onsuccess = (event: Event) => {
        console.log(`Item added to cart: Event #${eventId}, Category: ${category}`);
        resolve((event.target as IDBRequest).result as number);
      };
      
      request.onerror = (event: Event) => {
        const error = (event.target as IDBRequest).error;
        console.error('Error adding item to cart:', error);
        reject(error || new Error('Failed to add item to cart'));
      };
    });
  }
  
  /**
   * Remove an item from the cart by its ID
   * @param {number} id - The ID of the cart item to remove
   * @returns {Promise<void>} - Resolves when the item is removed
   */
  async removeFromCart(id: number): Promise<void> {
    await this.init();
    
    return new Promise<void>((resolve, reject) => {
      if (!this.db) {
        return reject(new Error('Database not initialized'));
      }
      
      const transaction = this.db.transaction([CART_STORE], 'readwrite');
      const store = transaction.objectStore(CART_STORE);
      
      const request = store.delete(id);
      
      request.onsuccess = () => {
        console.log(`Item #${id} removed from cart`);
        resolve();
      };
      
      request.onerror = (event: Event) => {
        const error = (event.target as IDBRequest).error;
        console.error('Error removing item from cart:', error);
        reject(error || new Error('Failed to remove item from cart'));
      };
    });
  }
  
  /**
   * Get all items in the cart
   * @returns {Promise<CartItem[]>} - Resolves with an array of cart items
   */
  async getAllCartItems(): Promise<CartItem[]> {
    await this.init();
    
    return new Promise<CartItem[]>((resolve, reject) => {
      if (!this.db) {
        return reject(new Error('Database not initialized'));
      }
      
      const transaction = this.db.transaction([CART_STORE], 'readonly');
      const store = transaction.objectStore(CART_STORE);
      
      const request = store.getAll();
      
      request.onsuccess = (event: Event) => {
        resolve((event.target as IDBRequest).result as CartItem[]);
      };
      
      request.onerror = (event: Event) => {
        const error = (event.target as IDBRequest).error;
        console.error('Error getting cart items:', error);
        reject(error || new Error('Failed to get cart items'));
      };
    });
  }
  
  /**
   * Get cart items by event ID
   * @param {number} eventId - The event ID to search for
   * @returns {Promise<CartItem[]>} - Resolves with an array of matching cart items
   */
  async getCartItemsByEvent(eventId: number): Promise<CartItem[]> {
    await this.init();
    
    return new Promise<CartItem[]>((resolve, reject) => {
      if (!this.db) {
        return reject(new Error('Database not initialized'));
      }
      
      const transaction = this.db.transaction([CART_STORE], 'readonly');
      const store = transaction.objectStore(CART_STORE);
      const index = store.index('eventId');
      
      const request = index.getAll(eventId);
      
      request.onsuccess = (event: Event) => {
        resolve((event.target as IDBRequest).result as CartItem[]);
      };
      
      request.onerror = (event: Event) => {
        const error = (event.target as IDBRequest).error;
        console.error('Error getting cart items by event:', error);
        reject(error || new Error('Failed to get cart items by event'));
      };
    });
  }
  
  /**
   * Get cart items by category
   * @param {string} category - The category to search for
   * @returns {Promise<CartItem[]>} - Resolves with an array of matching cart items
   */
  async getCartItemsByCategory(category: string): Promise<CartItem[]> {
    await this.init();
    
    return new Promise<CartItem[]>((resolve, reject) => {
      if (!this.db) {
        return reject(new Error('Database not initialized'));
      }
      
      const transaction = this.db.transaction([CART_STORE], 'readonly');
      const store = transaction.objectStore(CART_STORE);
      const index = store.index('category');
      
      const request = index.getAll(category);
      
      request.onsuccess = (event: Event) => {
        resolve((event.target as IDBRequest).result as CartItem[]);
      };
      
      request.onerror = (event: Event) => {
        const error = (event.target as IDBRequest).error;
        console.error('Error getting cart items by category:', error);
        reject(error || new Error('Failed to get cart items by category'));
      };
    });
  }
  
  /**
   * Clear all items from the cart
   * @returns {Promise<void>} - Resolves when the cart is cleared
   */
  async clearCart(): Promise<void> {
    await this.init();
    
    return new Promise<void>((resolve, reject) => {
      if (!this.db) {
        return reject(new Error('Database not initialized'));
      }
      
      const transaction = this.db.transaction([CART_STORE], 'readwrite');
      const store = transaction.objectStore(CART_STORE);
      
      const request = store.clear();
      
      request.onsuccess = () => {
        console.log('Cart cleared successfully');
        resolve();
      };
      
      request.onerror = (event: Event) => {
        const error = (event.target as IDBRequest).error;
        console.error('Error clearing cart:', error);
        reject(error || new Error('Failed to clear cart'));
      };
    });
  }
  
  /**
   * Update an existing cart item
   * @param {number} id - The ID of the cart item to update
   * @param {number} eventId - The new event ID (optional)
   * @param {string} category - The new category (optional)
   * @returns {Promise<void>} - Resolves when the item is updated
   */
  async updateCartItem(id: number, eventId?: number, category?: string): Promise<void> {
    await this.init();
    
    return new Promise<void>((resolve, reject) => {
      if (!this.db) {
        return reject(new Error('Database not initialized'));
      }
      
      const transaction = this.db.transaction([CART_STORE], 'readwrite');
      const store = transaction.objectStore(CART_STORE);
      
      // First get the existing item
      const getRequest = store.get(id);
      
      getRequest.onsuccess = (event: Event) => {
        const item = (event.target as IDBRequest).result as CartItem;
        
        if (!item) {
          return reject(new Error(`Item with ID ${id} not found in cart`));
        }
        
        // Update the fields if provided
        if (eventId !== undefined && Number.isInteger(eventId)) {
          item.eventId = eventId;
        }
        
        if (category !== undefined && typeof category === 'string' && category.trim()) {
          item.category = category.trim();
        }
        
        // Put the updated item back
        const updateRequest = store.put(item);
        
        updateRequest.onsuccess = () => {
          console.log(`Cart item #${id} updated successfully`);
          resolve();
        };
        
        updateRequest.onerror = (event: Event) => {
          const error = (event.target as IDBRequest).error;
          console.error('Error updating cart item:', error);
          reject(error || new Error('Failed to update cart item'));
        };
      };
      
      getRequest.onerror = (event: Event) => {
        const error = (event.target as IDBRequest).error;
        console.error('Error retrieving cart item for update:', error);
        reject(error || new Error('Failed to retrieve cart item for update'));
      };
    });
  }
  
  /**
   * Count items in the cart
   * @returns {Promise<number>} - Resolves with the number of items in the cart
   */
  async getCartCount(): Promise<number> {
    await this.init();
    
    return new Promise<number>((resolve, reject) => {
      if (!this.db) {
        return reject(new Error('Database not initialized'));
      }
      
      const transaction = this.db.transaction([CART_STORE], 'readonly');
      const store = transaction.objectStore(CART_STORE);
      
      const request = store.count();
      
      request.onsuccess = (event: Event) => {
        resolve((event.target as IDBRequest).result as number);
      };
      
      request.onerror = (event: Event) => {
        const error = (event.target as IDBRequest).error;
        console.error('Error counting cart items:', error);
        reject(error || new Error('Failed to count cart items'));
      };
    });
  }
}

// Export a single instance to use throughout the application
const cartDB = new CartDatabase();
export default cartDB;