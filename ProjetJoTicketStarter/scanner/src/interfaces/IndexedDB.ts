/**
 * Cart Item Interface
 * Represents a single item in the shopping cart
 */
export interface CartItem {
    id?: number;  // Optional as it's auto-generated
    eventId: number;
    category: string;
    addedAt: string;
  }
  
  /**
   * Database Error Interface
   * Represents errors that can occur during database operations
   */
  export interface DBError extends Error {
    name: string;
    message: string;
    code?: number;
  }
  
  /**
   * Cart Database Interface
   * Defines the methods available on the cart database
   */
  export interface ICartDatabase {
    init(): Promise<void>;
    addToCart(eventId: number, category: string): Promise<number>;
    removeFromCart(id: number): Promise<void>;
    getAllCartItems(): Promise<CartItem[]>;
    getCartItemsByEvent(eventId: number): Promise<CartItem[]>;
    getCartItemsByCategory(category: string): Promise<CartItem[]>;
    clearCart(): Promise<void>;
    updateCartItem(id: number, eventId?: number, category?: string): Promise<void>;
    getCartCount(): Promise<number>;
  }