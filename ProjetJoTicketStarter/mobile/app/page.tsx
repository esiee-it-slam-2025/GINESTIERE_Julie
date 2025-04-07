"use client"
//import Image from "next/image";
import styles from "./page.module.css";
import "@/node_modules/flag-icons/css/flag-icons.min.css";
// import fetch  from "node-fetch";
// import {Response} from "node-fetch";
import React, { useState, useEffect } from "react";
import { Event } from "@/src/interfaces/events";
import { parseEvents } from "@/src/API/parseAPI";
import {GET as apiGET, POST as apiPOST} from "@/src/API/callAPI";
import NumberInput from "@/src/component/NumberInput/NumberInput";
import { getCookie } from "@/src/API/cookies";

export default function Home(req:any) {
  const [data, setData] = useState<Event[]>([]);
  const [selectedEvent, selectEvent] = useState<Event | undefined>(undefined);
  const [session, setSession] = useState<boolean>(false)
  
  useEffect( () => {
    const checkSession= async () => {
      const response = await apiGET("sessionCheck");
      console.log("Session Status",response)
      setSession(response.sessionValid)
    }
    const fetchTeams  = async () => {
      const response = await apiGET("events");
      const eventList : Event[] = parseEvents({apiOutput: response})
      if(eventList) {
        eventList.sort((a, b) => {
          if (a.start > b.start) {
              return 1;
          }
      
          if (a.start < b.start) {
              return -1;
          }
      
          return 0;
        });
        setData(eventList);
        console.log(eventList);
      }
    };
    fetchTeams();
    checkSession()
  }, []);

  function handleEventClick({event}:{event:Event}){
    if(selectedEvent == event){
      selectEvent(undefined)
    }else{
      selectEvent(event)
    }
  }

  return (
    <>
      <header className={styles.header}>
        <h1 className={styles.headerTitle}>Jeux Olympique de Paris</h1>
        { session ? 
            <a href="/compte">Mon Compte</a> :
          <div className={styles.authLinks}>
            <a href="/connexion">connexion</a>
            <p>/</p>
            <a href="/inscription">inscription</a>
          </div>
        }
      </header>
      <div className={styles.page}>
        {data.map((event, i) => (
          <div key={event.id} className={styles.eventItem}>
            <span className={styles.eventDate}>
              {new Date(event.start).getDate().toString().padStart(2, '0')}
              /
              {new Date(event.start).getMonth().toString().padStart(2, '0')}
              /
              {new Date(event.start).getFullYear()}
              &nbsp; à &nbsp;
              {new Date(event.start).getHours().toString().padStart(2, '0')}
              h
              {new Date(event.start).getMinutes().toString().padStart(2, '0')}
            </span>
            <div className={styles.eventFlags} onClick={() => handleEventClick({event:event})}>
              {event.team_home ? 
                <span 
                  key={event.team_home.code} 
                  className={`fi fi-${event.team_home.code.toLowerCase()} ${event.team_home.id === event.winner ? styles.teamWinner : styles.team}`}>
                </span> : 
                <span className={`fi ${styles.teamUnknown}`}>?</span>
              }
              <span className={styles.vs}>VS</span>
              {event.team_away ? 
                <span 
                  key={event.team_away.code} 
                  className={`fi fi-${event.team_away.code.toLowerCase()} ${event.team_away.id === event.winner ? styles.teamWinner : styles.team}`}>
                </span> : 
                <span className={`fi ${styles.teamUnknown}`}>?</span>
              }
            </div>
            {event.id === selectedEvent?.id && (
              <div className={styles.ticketControls}>
                <div className={styles.ticketType}>
                  <label htmlFor="silver" className={styles.ticketLabel}>Silver</label>
                  <button className={styles.ticketMinusPlusButton}>-</button>
                  <NumberInput id="silver" name="silver" className={styles.numberInput}/>
                  <button className={styles.ticketMinusPlusButton}>+</button>
                </div>
                <div className={styles.ticketType}>
                  <label htmlFor="gold" className={styles.ticketLabel}>Gold</label>
                  <button className={styles.ticketMinusPlusButton}>-</button>
                  <NumberInput id="gold" name="gold" className={styles.numberInput}/>
                  <button className={styles.ticketMinusPlusButton}>+</button>
                </div>
                <div className={styles.ticketType}>
                  <label htmlFor="platinium" className={styles.ticketLabel}>Platinium</label>
                  <button className={styles.ticketMinusPlusButton}>-</button>
                  <NumberInput id="platinium" name="platinium" className={styles.numberInput}/>
                  <button className={styles.ticketMinusPlusButton}>+</button>
                </div>
                <button 
                  className={styles.addToCartButton} 
                  type="submit" 
                  disabled={!session}>
                  Ajouter au panier
                </button>
              </div>
            )}
          </div>
        ))}
      </div>
    </>
  );
}