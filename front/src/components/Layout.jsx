import React from 'react';
import { Link, Outlet } from 'react-router-dom';
import { FaHome, FaUser, FaNewspaper, FaNetworkWired } from 'react-icons/fa';

const Layout = () => {
  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <div className="w-64 bg-gray-800 text-white">
        <div className="p-4">
          <div className="flex flex-col items-center justify-center">
          <img src="/logo.svg" alt="AlgoAlchemy" className="w-10 h-10" />
          <h1 className="text-2xl font-bold">AlgoAlchemy</h1>
          <p className="text-gray-400 text-sm">Data Structures Visualizer</p>
          </div>
        </div>
        <nav className="mt-6">
          <ul>
            <li className="px-4 py-2 hover:bg-gray-700">
              <Link to="/" className="flex items-center">
                <FaHome className="mr-3" />
                <span>Dashboard</span>
              </Link>
            </li>
            <li className="px-4 py-2 hover:bg-gray-700">
              <Link to="/users" className="flex items-center">
                <FaUser className="mr-3" />
                <span>Users</span>
              </Link>
            </li>
            <li className="px-4 py-2 hover:bg-gray-700">
              <Link to="/blogposts" className="flex items-center">
                <FaNewspaper className="mr-3" />
                <span>Blog Posts</span>
              </Link>
            </li>
            <li className="px-4 py-2 hover:bg-gray-700">
              <span className="block text-gray-400 px-4 py-2">Data Structures</span>
              <ul className="pl-4">
                <li className="px-4 py-2 hover:bg-gray-700">
                  <Link to="/visualize/bst" className="flex items-center">
                    <FaNetworkWired className="mr-3" />
                    <span>Binary Search Tree</span>
                  </Link>
                </li>
                <li className="px-4 py-2 hover:bg-gray-700">
                  <Link to="/visualize/linkedlist" className="flex items-center">
                    <FaNetworkWired className="mr-3" />
                    <span>Linked List</span>
                  </Link>
                </li>
                <li className="px-4 py-2 hover:bg-gray-700">
                  <Link to="/visualize/stack" className="flex items-center">
                    <FaNetworkWired className="mr-3" />
                    <span>Stack</span>
                  </Link>
                </li>
                <li className="px-4 py-2 hover:bg-gray-700">
                  <Link to="/visualize/queue" className="flex items-center">
                    <FaNetworkWired className="mr-3" />
                    <span>Queue</span>
                  </Link>
                </li>
                <li className="px-4 py-2 hover:bg-gray-700">
                  <Link to="/visualize/hashmap" className="flex items-center">
                    <FaNetworkWired className="mr-3" />
                    <span>HashMap</span>
                  </Link>
                </li>
              </ul>
            </li>
          </ul>
        </nav>
      </div>

      {/* Main Content */}
      <div className="flex-1 overflow-y-auto">
        <header className="bg-white shadow">
          <div className="px-4 py-6">
            <h2 className="text-xl font-semibold text-gray-800">AlgoAlchemy Dashboard</h2>
          </div>
        </header>
        <main className="p-6">
          <Outlet />
        </main>
      </div>
    </div>
  );
};

export default Layout;
