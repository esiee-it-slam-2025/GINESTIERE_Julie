"use client"
//import Image from "next/image";
import styles from "./page.module.css";
import "@/node_modules/flag-icons/css/flag-icons.min.css";
// import fetch  from "node-fetch";
// import {Response} from "node-fetch";
import React, { useState, useEffect } from "react";
import { CSSProperties } from "react";
import { Event } from "@/src/interfaces/events";
import { parseEvents } from "@/src/API/parseAPI";
import {api} from "@/src/API/callAPI";
import { ChangeEvent } from "react";
import NumberInput from "@/src/component/NumberInput/NumberInput";



export default function Home(req:any) {

  const [data, setData] = useState<Event[]>([]);
  const [selectedEvent, selectEvent] = useState<Event | undefined>(undefined);
  

  useEffect( () => {
    const fetchTeams  = async () => {
    const response = await api.GET("events");
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
    
  }, []);
  function handleEventClick({event}:{event:Event}){
    if(selectedEvent == event){
      selectEvent(undefined)
    }else{
      selectEvent(event)
    }
  }

  const intInput : CSSProperties = {
    width:"2em",
    textAlign:"right",
  }
  const Team : CSSProperties = {
    fontSize: "5em",
    // margin: "0 auto",
    //height: "150%",
    width: "150%",
    transform: "translateY(25%)",
  }
  const TeamWinner : CSSProperties = {
    fontSize: "5em",
    //height: "150%",
    width: "150%",
    // margin: "0 auto",
    // transform: "translateY(30%)",
  }
  const TeamUnknown : CSSProperties = {
    fontSize: "2em",
  }
  const EventFlags : CSSProperties = {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    margin: "1em 0",
    overflow: "hidden",
    height: "5em",
    borderTop: "black 1px solid",
    borderLeft: "black 1px solid",
    borderRight: "black 1px solid",
    // padding: "0.5em 0.5em",
    width: "100%",
    borderRadius: "5px",
    backgroundColor: "#ffffff0f",
    WebkitMaskImage: "linear-gradient(to bottom, rgba(0, 0, 0, 1) 75%, rgba(0, 0, 0, 0) 95%)",
    maskImage: "linear-gradient(to bottom, rgba(0, 0, 0, 1) 75%, rgba(0, 0, 0, 0) 95%)",

  }
  const EventItems : CSSProperties = {
    width: "100%",
    cursor: "pointer",
  }
  const EventList : CSSProperties = {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fill, minmax(250px, 1fr))",
  }
  const header : CSSProperties ={
    display:"flex"
  }


  
  

  
  return (
    <>
      <header style={header}>
        <h1 style={{flex:1}}>Jeux Olympique de Paris</h1>
        <a href="/connexion">connexion</a>
        <p>/</p>
        <a href="/inscription">inscription</a>
      </header>
      <div className={styles.page + " MatchList"} style={EventList}>
        {data.map((event, i) => (
          <div key={event.id} style={EventItems} >
            <span>
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
            <div style={EventFlags} onClick={() => handleEventClick({event:event})}>
              {event.team_home ? <span key={event.team_home.code} className={`fi fi-${event.team_home.code.toLowerCase()}`} style={event.team_home.id === event.winner ? TeamWinner : Team}></span> : <span className={"fi"} style={TeamUnknown}>?</span>}
              <span className="vs">VS</span>
              {event.team_away ? <span key={event.team_away.code} className={`fi fi-${event.team_away.code.toLowerCase()}`} style={event.team_away.id === event.winner ? TeamWinner : Team}></span> : <span className={"fi"} style={TeamUnknown}>?</span>}
            </div>
            <div hidden={event.id !=selectedEvent?.id}>
              <div>
                <label htmlFor="silver">Silver</label>
                <button className={styles.ticketMinusPlusButton}>-</button>
                <NumberInput id="silver" name="silver" style={intInput}/>
                <button className={styles.ticketMinusPlusButton}>+</button>
              </div>
              <div>
                <label htmlFor="gold">Gold</label>
                <button className={styles.ticketMinusPlusButton}>-</button>
                <NumberInput id="gold" name="gold" style={intInput}/>
                <button className={styles.ticketMinusPlusButton}>+</button>
              </div>
              <div>
                <label htmlFor="platinium">Platinium</label>
                <button className={styles.ticketMinusPlusButton}>-</button>
                <NumberInput id="platinium" name="platinium" style={intInput}/>
                <button className={styles.ticketMinusPlusButton}>+</button>

                <button type="submit">Ajouter au panier</button>
              </div>
            </div>
          </div>
        ))}
        
      </div>
    </>
  );
}
