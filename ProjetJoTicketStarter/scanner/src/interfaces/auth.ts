import { Response } from "node-fetch";
/*export interface ApiResponse{
  status: number;
  success: boolean;  // Boolean flag indicating overall success
  ok: boolean;       // Alternative to success, aligns with fetch API's Response.ok
  message?: string;
  timestamp?: string;
  error:string;
}*/
export interface LoginCredentials {
  username: string;
  password: string;
}

export interface LoginResponse extends Response {
  success: boolean;
  user?: {
    username: string;
    id?: number;
    email?: string;
    // Add other user properties as needed
  };
  error?: string;
}

// You can extend this with more auth-related interfaces