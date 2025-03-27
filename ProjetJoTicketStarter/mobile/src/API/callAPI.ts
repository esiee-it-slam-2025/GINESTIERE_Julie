"use client"
import { promises } from "dns";
import { getCookie } from "./cookies";
const API_LINK = "http://localhost:8000/api/"

export const api = {
    GET: async (endpoint: string) : Promise<any> => {
        var r: any;
        return fetch(API_LINK + endpoint, {method: "GET",headers: {
            "Content-type": "application/json",
            "X-CSRFToken": getCookie("csrftoken") as string,
            // "CORS": "no-cors",
        }})
            .then((response) => {
                if(!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json()
            })
            .then((data) => {
                console.log("Fetched data:", data);
                return data;
            })
            .catch((error) => {
                console.error("There has been a problem with your fetch operation:", error);
                return [];
            });
    },
    POST: (endpoint: string, data: any) => {
        var response;
        fetch(API_LINK + endpoint, {
            method: "POST",
            credentials: "include",
            headers: {
                "Content-type": "application/json",
                "X-CSRFToken": getCookie("csrftoken") as string,
            },
            body: JSON.stringify(data),
        })
            .then((response) => {
                if(!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json()
            })
            .then((data) => {
                response = data;
            })
            .catch((error) => {
            console.error("There has been a problem with your fetch operation:", error);
            });
        return response;
}
}