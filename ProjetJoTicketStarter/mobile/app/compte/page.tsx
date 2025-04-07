"use client"

import styles from './page.module.css'


import {GET} from "@/src/API/callAPI"
export default function pages(){
    return <>
        <button className={styles.logoutButton} onClick={() => {GET("logout")}}>
            Déconnection
        </button>
    </>
}