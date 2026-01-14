
const BACKEND_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:2405/api/v1';
const CREWAI_URL = import.meta.env.VITE_CREWAI_URL || 'http://localhost:8000';

const configs = {
    BACKEND_URL: BACKEND_URL,
    CREWAI_URL: CREWAI_URL,
}

export default configs ;
