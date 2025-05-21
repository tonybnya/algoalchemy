import React, { useState, useEffect, useRef } from 'react';
import * as d3 from 'd3';
import { blogPostApi } from '../api/client';

const BSTVisualization = () => {
  const [blogPosts, setBlogPosts] = useState([]);
  const [bstNodes, setBstNodes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchId, setSearchId] = useState('');
  const [searchResult, setSearchResult] = useState(null);
  const [searchStatus, setSearchStatus] = useState('');
  
  const svgRef = useRef();
  const width = 800;
  const height = 500;
  
  useEffect(() => {
    const fetchBlogPosts = async () => {
      try {
        setLoading(true);
        const response = await blogPostApi.getNumericPosts();
        setBlogPosts(response.data);
        
        // Initialize BST with shuffled blog posts
        const shuffled = [...response.data].sort(() => 0.5 - Math.random());
        initializeBST(shuffled);
      } catch (err) {
        console.error('Error fetching blog posts:', err);
        setError('Failed to load blog posts. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchBlogPosts();
  }, []);
  
  // BST Node class for internal representation
  class TreeNode {
    constructor(data) {
      this.data = data;
      this.left = null;
      this.right = null;
    }
  }
  
  // BST implementation
  const initializeBST = (posts) => {
    let root = null;
    let nodes = [];
    
    const insertNode = (node, data) => {
      const id = data.id;
      
      if (node === null) {
        return new TreeNode(data);
      }
      
      if (id < node.data.id) {
        node.left = insertNode(node.left, data);
      } else if (id > node.data.id) {
        node.right = insertNode(node.right, data);
      }
      
      return node;
    };
    
    // Insert each blog post into the BST
    for (const post of posts) {
      root = insertNode(root, post);
    }
    
    // Convert the tree to a format that D3 can use
    const generateD3Tree = (node, x = width / 2, y = 50, level = 0) => {
      if (node === null) return;
      
      const newNode = {
        id: node.data.id,
        title: node.data.title,
        x: x,
        y: y,
        level: level
      };
      
      nodes.push(newNode);
      
      const gap = width / Math.pow(2, level + 2);
      
      if (node.left) generateD3Tree(node.left, x - gap, y + 80, level + 1);
      if (node.right) generateD3Tree(node.right, x + gap, y + 80, level + 1);
    };
    
    generateD3Tree(root);
    setBstNodes(nodes);
  };
  
  const renderBST = () => {
    if (!svgRef.current || bstNodes.length === 0) return;
    
    // Clear previous visualization
    d3.select(svgRef.current).selectAll("*").remove();
    
    const svg = d3.select(svgRef.current)
      .attr("width", width)
      .attr("height", height);
    
    // Draw edges (lines) between nodes
    const links = [];
    
    for (let i = 0; i < bstNodes.length; i++) {
      const node = bstNodes[i];
      
      // Find children
      const leftChild = bstNodes.find(n => 
        n.level === node.level + 1 && 
        n.x < node.x && 
        Math.abs(n.x - node.x) < width / Math.pow(2, node.level + 1) + 10
      );
      
      const rightChild = bstNodes.find(n => 
        n.level === node.level + 1 && 
        n.x > node.x && 
        Math.abs(n.x - node.x) < width / Math.pow(2, node.level + 1) + 10
      );
      
      if (leftChild) {
        links.push({ source: node, target: leftChild });
      }
      
      if (rightChild) {
        links.push({ source: node, target: rightChild });
      }
    }
    
    // Draw the links
    svg.selectAll(".link")
      .data(links)
      .enter()
      .append("line")
      .attr("class", "link")
      .attr("x1", d => d.source.x)
      .attr("y1", d => d.source.y)
      .attr("x2", d => d.target.x)
      .attr("y2", d => d.target.y)
      .attr("stroke", "#999")
      .attr("stroke-width", 2);
    
    // Create node groups
    const nodes = svg.selectAll(".node")
      .data(bstNodes)
      .enter()
      .append("g")
      .attr("class", "node")
      .attr("transform", d => `translate(${d.x}, ${d.y})`);
    
    // Draw circles for nodes
    nodes.append("circle")
      .attr("r", 25)
      .attr("fill", d => {
        if (searchResult && d.id === searchResult.id) {
          return "#4CAF50"; // Green for found node
        }
        return "#3182CE"; // Default blue
      })
      .attr("stroke", "#fff")
      .attr("stroke-width", 2);
    
    // Add text (IDs) to nodes
    nodes.append("text")
      .attr("text-anchor", "middle")
      .attr("dy", ".3em")
      .attr("fill", "#fff")
      .text(d => d.id);
    
    // Add titles as tooltips
    nodes.append("title")
      .text(d => `ID: ${d.id}\nTitle: ${d.title}`);
  };
  
  useEffect(() => {
    renderBST();
  }, [bstNodes, searchResult]);
  
  const handleSearch = (e) => {
    e.preventDefault();
    
    const id = parseInt(searchId);
    if (isNaN(id)) {
      setSearchStatus('Please enter a valid numeric ID');
      setSearchResult(null);
      return;
    }
    
    // Perform search in the BST visualization
    const found = bstNodes.find(node => node.id === id);
    
    if (found) {
      setSearchResult(found);
      setSearchStatus(`Blog post with ID ${id} found!`);
    } else {
      setSearchResult(null);
      setSearchStatus(`Blog post with ID ${id} not found.`);
    }
  };
  
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
      <h1 className="text-2xl font-bold mb-6">Binary Search Tree Visualization</h1>
      
      <div className="bg-white shadow-md rounded-lg p-6 mb-6">
        <h2 className="text-xl font-semibold mb-4">About Binary Search Trees</h2>
        <p className="mb-4">
          A Binary Search Tree (BST) is a data structure that organizes values in a hierarchical manner.
          Each node has at most two children: a left child with a value less than the parent node,
          and a right child with a value greater than the parent node.
        </p>
        <p>
          In this visualization, blog post IDs are used as node values. Searching for a post by ID
          traverses the tree according to the BST property.
        </p>
      </div>
      
      <div className="bg-white shadow-md rounded-lg p-6 mb-6">
        <h2 className="text-xl font-semibold mb-4">Search for a Blog Post by ID</h2>
        <form onSubmit={handleSearch} className="mb-4 flex">
          <input
            type="text"
            value={searchId}
            onChange={(e) => setSearchId(e.target.value)}
            placeholder="Enter blog post ID"
            className="shadow appearance-none border rounded flex-1 py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
          <button
            type="submit"
            className="ml-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          >
            Search
          </button>
        </form>
        
        {searchStatus && (
          <div className={`p-4 rounded mb-4 ${
            searchResult ? 'bg-green-100 text-green-700' : 'bg-yellow-100 text-yellow-700'
          }`}>
            <p>{searchStatus}</p>
          </div>
        )}
        
        {searchResult && (
          <div className="p-4 bg-gray-100 rounded">
            <h3 className="font-semibold mb-2">Found Blog Post:</h3>
            <p><span className="font-medium">ID:</span> {searchResult.id}</p>
            <p><span className="font-medium">Title:</span> {searchResult.title}</p>
          </div>
        )}
      </div>
      
      <div className="bg-white shadow-md rounded-lg p-6 overflow-auto">
        <h2 className="text-xl font-semibold mb-4">BST Visualization</h2>
        {bstNodes.length > 0 ? (
          <div className="flex justify-center">
            <svg ref={svgRef}></svg>
          </div>
        ) : (
          <p className="text-center text-gray-500">No data available for visualization.</p>
        )}
      </div>
    </div>
  );
};

export default BSTVisualization;
