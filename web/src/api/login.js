import http from '@/utils/http'

export function login (username, password) {
    return http.post('/api/users/login', { username, password })
}

