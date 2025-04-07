"use client"

import styles from './page.module.css'
import { useRouter } from 'next/navigation'
import { useEffect, useState } from 'react'
import {GET as apiGET} from "@/src/API/callAPI"


import {GET} from "@/src/API/callAPI"
export default function pages(){
    const [session, setSession] = useState<boolean | undefined>(undefined)
    const router = useRouter()
    
    useEffect(()=>{
        const checkSession= async () => {
            const response = await apiGET("sessionCheck");
            console.log("Session Status",response)
            setSession(response.sessionValid)
            if(response.sessionValid === false){
              router.push("/")
            }
            
          }
          checkSession()
      },[])


    if(session === undefined){
        return<>
            <span>Loading ...</span>
        </>
    }
    if(session === false){
        return<><span>Déconnecté</span></>
    }

    return <>
        <button className={styles.logoutButton} onClick={() => {
            GET("logout");
            router.push("/")
        }}>
            Déconnection
        </button>
    </>
}