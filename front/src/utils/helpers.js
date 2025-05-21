/**
 * Format error messages from API responses
 * @param {Error} error - The error object from axios
 * @returns {string} Formatted error message
 */
export const formatErrorMessage = (error) => {
  if (error.response && error.response.data && error.response.data.message) {
    return error.response.data.message;
  }
  return error.message || 'An unknown error occurred';
};

/**
 * Truncate a string to a specified length and add ellipsis if truncated
 * @param {string} str - The string to truncate
 * @param {number} length - The maximum length
 * @returns {string} Truncated string
 */
export const truncateString = (str, length = 50) => {
  if (!str) return '';
  return str.length > length ? str.substring(0, length) + '...' : str;
};

/**
 * Parse a date string into a formatted date string
 * @param {string} dateString - The date string to parse
 * @returns {string} Formatted date string
 */
export const formatDate = (dateString) => {
  if (!dateString) return '';
  
  const date = new Date(dateString);
  if (isNaN(date.getTime())) return dateString;
  
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
};

/**
 * Generate a random color for visualization elements
 * @returns {string} Hex color code
 */
export const getRandomColor = () => {
  const colors = [
    '#4299E1', // blue-500
    '#48BB78', // green-500
    '#ED8936', // orange-500
    '#9F7AEA', // purple-500
    '#F56565', // red-500
    '#ECC94B', // yellow-500
    '#38B2AC', // teal-500
    '#ED64A6', // pink-500
  ];
  
  return colors[Math.floor(Math.random() * colors.length)];
};

/**
 * Check if an object is empty
 * @param {Object} obj - The object to check
 * @returns {boolean} True if the object is empty
 */
export const isEmptyObject = (obj) => {
  return obj && Object.keys(obj).length === 0 && obj.constructor === Object;
};
