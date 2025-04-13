"use client"
import { promises } from "dns";
import { getCookie } from "./cookies";

/**** .env ****/
require("dotenv").config();
const API_LINK : string = process.env.API_LINK || "http://localhost:8000/api/";

const buildHeaders = () =>{
    return {"Content-type": "application/json",
    "X-CSRFToken": getCookie("csrftoken") as string,
    }
}



export const GET = (endpoint: string) : Promise<any> => {
    return fetch(API_LINK + endpoint,
        {
            method: "GET",
            credentials: "include",
            headers: buildHeaders(),
        })
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
}
export const POST = (endpoint: string, data: any) : Promise<any> => {
    var response = fetch(API_LINK + endpoint, {
        method: "POST",
        credentials: "include",
        headers: buildHeaders(),
        body: JSON.stringify(data),
    })
        .then((response) => {
            // if(!response.ok) {
            //     throw new Error(response.statusText || `API request failed with status: ${response.status}`);
            // }
            return response.json()
        })
        .then((data) => {
            //response = data;
            console.log("response data" + data)
            return data
        })
        .catch((error) => {
            response = error
            console.error("There has been a problem with your fetch operation:", error);
            return { success: false, error: error.message };
        });

    return response
}
