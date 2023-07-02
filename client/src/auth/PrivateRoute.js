import {Navigate, Route} from 'react-router-dom';
import { useContext } from "react";
import { AuthContext } from "./AuthContext";
import { Spin } from 'antd';

const PrivateRoute = ({children}) => {
    const { isAuthenticated, loading } = useContext(AuthContext);
    if (loading){
        return <Spin/>
    }
    console.log("isAuthenticated", isAuthenticated)
    return isAuthenticated ? children : <Navigate to="/login" replace />;
}

export default PrivateRoute;