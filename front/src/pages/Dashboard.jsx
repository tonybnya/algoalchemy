import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { userApi, blogPostApi } from "../api/client";

const Dashboard = () => {
  const [stats, setStats] = useState({
    userCount: "...",
    blogPostCount: "...",
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        setLoading(true);
        // Fetch users
        const usersResponse = await userApi.getUsersAscending();
        const users = usersResponse.data;

        // Try to get numeric posts to count blog posts
        let blogPosts = [];
        try {
          const blogPostsResponse = await blogPostApi.getNumericPosts();
          blogPosts = blogPostsResponse.data;
        } catch (err) {
          console.error("Error fetching blog posts:", err);
        }

        setStats({
          userCount: users.length,
          blogPostCount: blogPosts.length,
        });
      } catch (err) {
        console.error("Error fetching dashboard data:", err);
        setError("Failed to load dashboard data. Please try again later.");
      } finally {
        setLoading(false);
      }
    };

    fetchStats();
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
        <p>{error}</p>
      </div>
    );
  }

  return (
    <div>
      <h1 className="text-2xl font-bold text-gray-800 mb-6">Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
        {/* Users Card */}
        <div className="bg-white shadow-md rounded-lg p-6">
          <h2 className="text-xl font-semibold text-gray-800 mb-2">Users</h2>
          <p className="text-4xl font-bold text-blue-600 mb-4">
            {stats.userCount}
          </p>
          <Link
            to="/users"
            className="inline-block bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded"
          >
            Manage Users
          </Link>
        </div>

        {/* Blog Posts Card */}
        <div className="bg-white shadow-md rounded-lg p-6">
          <h2 className="text-xl font-semibold text-gray-800 mb-2">Blog Posts</h2>
          <p className="text-4xl font-bold text-green-600 mb-4">
            {stats.blogPostCount}
          </p>
          <Link
            to="/blogposts"
            className="inline-block bg-green-500 hover:bg-green-600 text-white py-2 px-4 rounded"
          >
            Manage Blog Posts
          </Link>
        </div>

        {/* Data Structures Card */}
        <div className="bg-white shadow-md rounded-lg p-6">
          <h2 className="text-xl font-semibold text-gray-800 mb-2">Data Structures</h2>
          <p className="text-lg text-gray-600 mb-4">
            Visualize and interact with various data structures
          </p>
          <div className="space-y-2">
            <Link
              to="/visualize/bst"
              className="block bg-purple-500 hover:bg-purple-600 text-white py-2 px-4 rounded"
            >
              Binary Search Tree
            </Link>
            <Link
              to="/visualize/linkedlist"
              className="block bg-indigo-500 hover:bg-indigo-600 text-white py-2 px-4 rounded"
            >
              Linked List
            </Link>
            <Link
              to="/visualize/stack"
              className="block bg-pink-500 hover:bg-pink-600 text-white py-2 px-4 rounded"
            >
              Stack
            </Link>
            <Link
              to="/visualize/queue"
              className="block bg-yellow-500 hover:bg-yellow-600 text-white py-2 px-4 rounded"
            >
              Queue
            </Link>
            <Link
              to="/visualize/hashmap"
              className="block bg-teal-500 hover:bg-teal-600 text-white py-2 px-4 rounded"
            >
              HashMap
            </Link>
          </div>
        </div>
      </div>

      <div className="bg-white shadow-md rounded-lg p-6">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">About AlgoAlchemy</h2>
        <p className="text-gray-600 mb-4 text-justify">
          AlgoAlchemy is a platform for visualizing, manipulating, and
          interacting with various data structures and algorithms. This
          dashboard provides an interface to explore the implementation of
          different data structures like Binary Search Trees, Linked Lists,
          Stacks, Queues, and HashMaps.
        </p>
        <p className="text-gray-600 mb-4 text-justify">
          You can also manage users and blog posts, which are stored in the
          backend and can be manipulated through these data structures.
        </p>
      </div>
    </div>
  );
};

export default Dashboard;
