import React from 'react'

export default async function useCatch(callback) {
    try {
        await callback();
    } catch (error) {
        // Log error for debugging instead of opening external AI service
        console.error('[Javascript Error]:', error.message);
        console.error('Stack trace:', error.stack);
        
        // Optionally show a user-friendly error message
        alert(`An error occurred: ${error.message}\nCheck console for details.`);
    }
}