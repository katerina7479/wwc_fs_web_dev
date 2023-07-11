import axios from 'axios'
import { BASE_API_URL } from '../constants'

axios.interceptors.response.use(
  function (response) {
    // If the request succeeds, we don't have to do anything and just return the response
    return response
  },
  function (error) {
    const originalRequest = error.config
    // If the server response was a 401, Access Token is expired, and we need to refresh

    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      console.log('Attempting to refresh tokens')
      // Attempt to refresh the token
      return axios
        .post(`${BASE_API_URL}/auth/refresh/`, {
          refresh: localStorage.getItem('refresh')
        })
        .then((response) => {
          if (response.status === 200) {
            // If refresh was successful, update AccessToken in local storage
            localStorage.setItem('access', response.data.access)

            // Update the Authorization on axios
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('access')

            // Retry the original request
            originalRequest.headers['Authorization'] = 'Bearer ' + localStorage.getItem('access')
            return axios(originalRequest)
          }
        })
    }

    // If the request fails for reasons other than an expired token, we just reject the promise
    return Promise.reject(error)
  }
)

export default axios
