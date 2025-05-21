import axios from 'axios';

// Base URL for the API - use environment variable or fallback to localhost:5000
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add response interceptor for error handling
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

// User API endpoints
export const userApi = {
  // Get all users in ascending order
  getUsersAscending: () => apiClient.get('/users/ascending_id'),
  
  // Get all users in descending order
  getUsersDescending: () => apiClient.get('/users/descending_id'),
  
  // Get a specific user by ID
  getUser: (userId) => apiClient.get(`/users/${userId}`),
  
  // Create a new user
  createUser: (userData) => apiClient.post('/users', userData),
  
  // Update a user
  updateUser: (userId, userData) => apiClient.put(`/users/${userId}`, userData),
  
  // Delete a user
  deleteUser: (userId) => apiClient.delete(`/users/${userId}`),
  
  // Get all blog posts for a user
  getUserBlogPosts: (userId) => apiClient.get(`/users/${userId}/blogposts`),
};

// BlogPost API endpoints
export const blogPostApi = {
  // Create a new blog post for a specific user
  createBlogPost: (userId, postData) => apiClient.post(`/blogposts/${userId}`, postData),
  
  // Get a specific blog post by ID
  getBlogPost: (postId) => apiClient.get(`/blogposts/${postId}`),
  
  // Get numeric post bodies
  getNumericPosts: () => apiClient.get('/blogposts/numerics'),
  
  // Delete the last 10 blog posts
  deleteLast10Posts: () => apiClient.delete('/blogposts/delete_last_10'),
};

export default apiClient;
