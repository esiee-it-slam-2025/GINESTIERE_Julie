"use client"

import styles from './page.module.css'
import { useRouter } from 'next/navigation'
import { useEffect, useState } from 'react'
import {GET as apiGET} from "@/src/API/callAPI"
import { Ticket } from '@/src/interfaces/tickets'
import QRCode from '@/src/component/QRCode/QRCode'



import {GET} from "@/src/API/callAPI"
export default function pages(){
    const [session, setSession] = useState<boolean | undefined>(undefined)
    const [page, setPage] = useState<number>(0)
    const [tickets, setTickets] = useState<Ticket[]>([])
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
        const fetchTickets = async () => {
            const response = await apiGET("tickets");
            setTickets(response)
        }
          checkSession()
          fetchTickets()
      },[])


    if(session === undefined){
        return<>
            <span>Loading ...</span>
        </>
    }
    if(session === false){
        return<><span>Déconnecté</span></>
    }

    return <div className={styles.container}>
        <div>
            <button onClick={() => setPage(0)}>
                Compte
            </button>
            <button onClick={() => setPage(1)}>
                Billets
            </button>
        </div>
        <div hidden={page != 0}>
            <button className={styles.logoutButton} onClick={() => {
                GET("logout");
                router.push("/")
            }}>
                Déconnection
            </button>
        </div>
        <div hidden={page != 1}>
            {tickets.length == 0 && <span>Vous n'avez aucun ticket</span>}
            {tickets.map((ticket, i)=>
            (
                <div key={i}>
                    <QRCode
                    value={ticket.uuid}
                    />
                    <div>
                    <span>
                        {ticket.event.stadium.name}
                    </span>
                    <span className={styles.eventDate}>
                        {new Date(ticket.event.start).getDate().toString().padStart(2, '0')}
                        /
                        {new Date(ticket.event.start).getMonth().toString().padStart(2, '0')}
                        /
                        {new Date(ticket.event.start).getFullYear()}
                        &nbsp; à &nbsp;
                        {new Date(ticket.event.start).getHours().toString().padStart(2, '0')}
                        h
                        {new Date(ticket.event.start).getMinutes().toString().padStart(2, '0')}
                    </span>
                    </div>
                </div>
            )
            )}
        </div>
    </div>
}