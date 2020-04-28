import axios from 'axios'

export const http = axios.create({
  // baseURL: `http://127.0.0.1:9019/`,
  baseURL: `https://strawpoll-be.aiotools.ovh/`,
  timeout: 10000,
  headers: {
    // Authorization: 'Bearer {token}'
  }
})
