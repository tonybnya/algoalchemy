# AlgoAlchemy Frontend

This is the frontend UI for AlgoAlchemy, a platform to visualize, manipulate, and interact with various data structures and algorithms.

## Features

- User management (create, read, update, delete users)
- Blog post management (create, read, delete blog posts)
- Data structure visualizations:
  - Binary Search Tree
  - Linked List
  - Stack
  - Queue
  - HashMap

## Technologies Used

- React for UI components
- React Router for navigation
- Tailwind CSS for styling
- D3.js for data structure visualizations
- Axios for API requests

## Setup Instructions

### Prerequisites

- Node.js (v14 or higher)
- npm (v6 or higher)
- AlgoAlchemy API running on http://localhost:5000

### Installation

1. Clone the repository (if you haven't already)
2. Navigate to the `front` directory
3. Install dependencies:

```bash
npm install
```

4. Start the development server:

```bash
npm run dev
```

5. Open your browser and navigate to http://localhost:3000

### Building for Production

To build the application for production, run:

```bash
npm run build
```

The build files will be generated in the `dist` directory.

## API Connection

By default, the frontend connects to the AlgoAlchemy API at http://localhost:5000. 
If your API is running on a different port or host, update the `.env` file:

```
VITE_API_URL=http://your-api-host:port
```

## Data Structure Visualizations

The application provides interactive visualizations for various data structures:

- **Binary Search Tree**: Visualizes insertion and search operations
- **Linked List**: Shows adding to head/tail and traversal
- **Stack**: Demonstrates push and pop operations
- **Queue**: Illustrates enqueue and dequeue operations
- **HashMap**: Displays key-value storage with hash function visualization

## Project Structure

```
front/
├── public/            # Static files
├── src/
│   ├── api/           # API client and endpoints
│   ├── components/    # Reusable UI components
│   ├── pages/         # Main application pages
│   ├── utils/         # Utility functions
│   ├── visualizations/# Data structure visualization components
│   ├── App.jsx        # Main application component
│   ├── main.jsx       # Application entry point
│   └── index.css      # Global styles
└── README.md          # This file
```
