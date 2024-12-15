const API_URL = 'http://localhost:8001';

export async function getGuestsList() {
    const response = await fetch(`${API_URL}/orders`);
    return await response.json();
}
