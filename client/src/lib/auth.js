const tokenName = 'user-token'

export function setToken(token){
  localStorage.setItem(tokenName, token)
}

export function getToken(){
  return localStorage.getItem(tokenName)
}

export function removeToken(){
  localStorage.removeItem(tokenName)
}

export function isLoggedIn(){
  const token = getToken()
  if (!token) return false
  
  // Decode the token, to extract information from the payload
  const payloadStr = token.split('.')[1] // extract this middle string from the token (still base64 encoded)
  const payloadObj = JSON.parse(atob(payloadStr)) // decode the b64 string using atob, then convert the JSON string it returns to an object

  // Check the expiry date is valid (in the future)
  // If exp is bigger than now, it is in the future and valid
  if (payloadObj.exp > Date.now() / 1000) {
    return true
  } else {
    return false
  }

}