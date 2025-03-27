"use client"

export function getCookie(name:string) {
    const cookies = document.cookie.split("; ");
    for (const cookie of cookies) {
      if (cookie.startsWith(`${name}=`)) {
        return decodeURIComponent(cookie.substring(name.length + 1));
      }
    }
  
}
