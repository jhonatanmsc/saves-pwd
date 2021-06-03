const API_URL = 'http://localhost:8000'

const parseUrl = (urlName, args=[]) => {
    switch(urlName) {
        case 'phrase-list': return `${API_URL}/`
        case 'phrase-detail': return `${API_URL}/${args[0]}`
        case 'phrase-create': return `${API_URL}/create-phrase`
        case 'phrase-update': return `${API_URL}/update-phrase/${args[0]}`
        case 'phrase-delete': return `${API_URL}/remove-phrase/${args[0]}`
        case 'phrase-decode': return `${API_URL}/decode-phrase/${args[0]}`
    }
}

export {API_URL, parseUrl}