// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyC2CU8CdjeRtNegha3lSANpRwfPG-aHVwI",
  authDomain: "sql-optimization-71006.firebaseapp.com",
  projectId: "sql-optimization-71006",
  storageBucket: "sql-optimization-71006.appspot.com",
  messagingSenderId: "250978855598",
  appId: "1:250978855598:web:4a87bed2771c34f4e91b3f",
  measurementId: "G-8DXTBM4339"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);