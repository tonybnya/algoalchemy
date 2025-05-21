import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { blogPostApi, userApi } from '../api/client';
import { FaPlus, FaEye, FaTrash, FaCalculator } from 'react-icons/fa';

const BlogPosts = () => {
  const [blogPosts, setBlogPosts] = useState([]);
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [viewMode, setViewMode] = useState('normal'); // 'normal' or 'numeric'
  const [confirmDelete, setConfirmDelete] = useState(false);

  const fetchUsers = async () => {
    try {
      const response = await userApi.getUsersAscending();
      return response.data;
    } catch (err) {
      console.error('Error fetching users:', err);
      return [];
    }
  };

  const fetchNumericPosts = async () => {
    try {
      setLoading(true);
      const response = await blogPostApi.getNumericPosts();
      setBlogPosts(response.data);
      setViewMode('numeric');
    } catch (err) {
      console.error('Error fetching numeric posts:', err);
      setError('Failed to load numeric blog posts. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  const fetchBlogPosts = async () => {
    try {
      setLoading(true);
      
      // Since we don't have a direct API to get all posts,
      // we'll need to get them through the numeric posts endpoint
      // or handle a mock implementation
      const response = await blogPostApi.getNumericPosts();
      // For the normal view, we'll use the same data but treat the body as text
      // In a real implementation, you'd fetch the actual posts with text bodies
      setBlogPosts(response.data);
      setViewMode('normal');
    } catch (err) {
      console.error('Error fetching blog posts:', err);
      setError('Failed to load blog posts. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteLast10 = async () => {
    try {
      await blogPostApi.deleteLast10Posts();
      // Refresh posts
      if (viewMode === 'numeric') {
        fetchNumericPosts();
      } else {
        fetchBlogPosts();
      }
      setConfirmDelete(false);
    } catch (err) {
      console.error('Error deleting posts:', err);
      setError('Failed to delete blog posts. Please try again later.');
    }
  };

  useEffect(() => {
    const loadData = async () => {
      try {
        setLoading(true);
        const usersData = await fetchUsers();
        setUsers(usersData);
        
        // Load posts based on view mode
        if (viewMode === 'numeric') {
          await fetchNumericPosts();
        } else {
          await fetchBlogPosts();
        }
      } catch (err) {
        console.error('Error loading data:', err);
        setError('Failed to load data. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  // Helper function to find username by user_id
  const getUsernameById = (userId) => {
    const user = users.find(u => u.id === userId);
    return user ? user.username : 'Unknown User';
  };

  if (loading && blogPosts.length === 0) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Blog Posts</h1>
        <div className="flex space-x-2">
          <button
            onClick={viewMode === 'normal' ? fetchNumericPosts : fetchBlogPosts}
            className={`inline-flex items-center py-2 px-4 rounded ${
              viewMode === 'numeric' 
                ? 'bg-blue-500 hover:bg-blue-600 text-white' 
                : 'bg-gray-200 hover:bg-gray-300 text-gray-800'
            }`}
          >
            <FaCalculator className="mr-2" />
            {viewMode === 'numeric' ? 'Normal View' : 'Numeric View'}
          </button>
          
          {users.length > 0 && (
            <div className="relative group">
              <button className="inline-flex items-center bg-green-500 hover:bg-green-600 text-white py-2 px-4 rounded">
                <FaPlus className="mr-2" />
                New Post
              </button>
              <div className="absolute right-0 mt-2 w-56 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 bg-white shadow-lg rounded-md overflow-hidden z-10">
                {users.map(user => (
                  <Link
                    key={user.id}
                    to={`/blogposts/new/${user.id}`}
                    className="block px-4 py-2 text-gray-800 hover:bg-gray-100"
                  >
                    {user.username}
                  </Link>
                ))}
              </div>
            </div>
          )}
          
          <button
            onClick={() => setConfirmDelete(true)}
            className="inline-flex items-center bg-red-500 hover:bg-red-600 text-white py-2 px-4 rounded"
          >
            <FaTrash className="mr-2" />
            Delete Last 10
          </button>
        </div>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          <p>{error}</p>
        </div>
      )}

      <div className="bg-white shadow-md rounded-lg overflow-hidden">
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  ID
                </th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Title
                </th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  {viewMode === 'numeric' ? 'Body (Numeric)' : 'Body'}
                </th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Author
                </th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Actions
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {blogPosts.length === 0 ? (
                <tr>
                  <td colSpan="5" className="px-6 py-4 text-center text-sm text-gray-500">
                    No blog posts found. Add a new post to get started.
                  </td>
                </tr>
              ) : (
                blogPosts.map((post) => (
                  <tr key={post.id} className="hover:bg-gray-50">
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                      {post.id}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {post.title}
                    </td>
                    <td className="px-6 py-4 text-sm text-gray-500">
                      <div className="max-w-xs truncate">
                        {viewMode === 'numeric' 
                          ? post.body 
                          : (typeof post.body === 'number' 
                              ? `Text with ASCII sum: ${post.body}` 
                              : post.body)
                        }
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {getUsernameById(post.user_id)}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                      <div className="flex space-x-2">
                        <Link 
                          to={`/blogposts/${post.id}`} 
                          className="text-blue-600 hover:text-blue-900"
                        >
                          <FaEye className="w-5 h-5" />
                        </Link>
                      </div>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Delete Confirmation Modal */}
      {confirmDelete && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-lg p-6 max-w-md w-full">
            <h3 className="text-lg font-semibold mb-4">Delete Last 10 Blog Posts</h3>
            <p className="mb-6">Are you sure you want to delete the last 10 blog posts? This action cannot be undone.</p>
            <div className="flex justify-end space-x-2">
              <button
                onClick={() => setConfirmDelete(false)}
                className="px-4 py-2 bg-gray-300 text-gray-800 rounded hover:bg-gray-400"
              >
                Cancel
              </button>
              <button
                onClick={handleDeleteLast10}
                className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default BlogPosts;
