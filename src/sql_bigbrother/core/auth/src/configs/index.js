const dev = {
    port: 2405,
    mongodbURL: process.env.MONGODB_URL || 'mongodb://127.0.0.1:27017/SQL_bigbrother',
    frontendURL: process.env.FRONTEND_URL || 'http://localhost:5173',
    backendURL: process.env.BACKEND_URL || 'http://localhost:2405'
}

const production = {
    port: 2405,
    mongodbURL: process.env.MONGODB_URL,
    frontendURL: process.env.FRONTEND_URL,
    backendURL: process.env.BACKEND_URL
}

const configs = { dev, production }
const env = process.env.NODE_ENV?.trim() || 'dev';
module.exports = configs[env];