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

    // Group tickets by event ID
    const groupTicketsByEvent = () => {
        const groupedTickets: { [key: number]: Ticket[] } = {};
        
        tickets.forEach(ticket => {
            const eventId = ticket.event.id;
            if (!groupedTickets[eventId]) {
                groupedTickets[eventId] = [];
            }
            groupedTickets[eventId].push(ticket);
        });
        
        return groupedTickets;
    };
    
    const ticketsByEvent = groupTicketsByEvent();


    if(session === undefined){
        return <div className={styles.loadingIndicator}>Loading ...</div>
    }
    if(session === false){
        return <div className={styles.loadingIndicator}>Déconnecté</div>
    }

    return <div className={styles.container}>
        <div className={styles.navButtons}>
            <button 
              className={`${styles.navButton} ${page === 0 ? styles.navButtonActive : ''}`} 
              onClick={() => setPage(0)}>
                Compte
            </button>
            <button 
              className={`${styles.navButton} ${page === 1 ? styles.navButtonActive : ''}`} 
              onClick={() => setPage(1)}>
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
            {tickets.length == 0 && <div className={styles.emptyTickets}>Vous n'avez aucun ticket</div>}
            <div className={styles.eventList}>
                {Object.entries(ticketsByEvent).map(([eventId, eventTickets]) => {
                    // Get event details from the first ticket
                    const event = eventTickets[0].event;
                    
                    return (
                        <div key={eventId} className={styles.eventGroup}>
                            <div className={styles.eventHeader}>
                                <div className={styles.eventInfo}>
                                    <span className={styles.stadiumName}>{event.stadium.name}</span>
                                    <span className={styles.eventDate}>
                                        {new Date(event.start).getDate().toString().padStart(2, '0')}
                                        /
                                        {(new Date(event.start).getMonth() + 1).toString().padStart(2, '0')}
                                        /
                                        {new Date(event.start).getFullYear()}
                                        &nbsp; à &nbsp;
                                        {new Date(event.start).getHours().toString().padStart(2, '0')}
                                        h
                                        {new Date(event.start).getMinutes().toString().padStart(2, '0')}
                                    </span>
                                </div>
                                
                                {/* Show teams if available */}
                                {(event.team_home || event.team_away) && (
                                    <div className={styles.matchTeams}>
                                        <span>{event.team_home?.name || "TBD"}</span>
                                        <span className={styles.versus}>vs</span>
                                        <span>{event.team_away?.name || "TBD"}</span>
                                        {event.score && <span className={styles.score}>{event.score}</span>}
                                    </div>
                                )}
                            </div>
                            
                            <div className={styles.ticketListByEvent}>
                                {eventTickets.map((ticket, i) => (
                                    <div key={i} className={styles.ticketItem}>
                                        <div className={styles.ticketContent}>
                                            <QRCode value={ticket.uuid} />
                                            <div className={styles.ticketInfo}>
                                                <span className={styles.ticketCategory}>
                                                    {ticket.category}
                                                </span>
                                                <span className={styles.ticketId}>
                                                    ID: {ticket.uuid.substring(0, 8)}...
                                                </span>
                                            </div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    );
                })}
            </div>
        </div>
    </div>
}