"use client"
import {GET} from "@/src/API/callAPI"
export default function pages(){
    return <>
        <button onClick={() => {GET("logout")}}>
            Déconnection
        </button>
    </>
}