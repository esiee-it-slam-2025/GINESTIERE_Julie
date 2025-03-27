"use client"
//import Image from "next/image";
import styles from "./page.module.css";
import "@/node_modules/flag-icons/css/flag-icons.min.css";
// import fetch  from "node-fetch";
// import {Response} from "node-fetch";
import React, { useState, useEffect } from "react";
import { CSSProperties } from "react";
import { Event } from "@/src/interfaces/events";
import {api} from "@/src/API/callAPI";



export default function Home(req:any) {

  const [data, setData] = useState<Event[]>([]);
  

  useEffect( () => {
    const fetchTeams  = async () => {
    const response : Event[]  = await api.GET("events") as Event[];
    await api.GET("events");
    if(response) {
      response.sort((a, b) => {
        if (a.start > b.start) {
            return 1;
        }
    
        if (a.start < b.start) {
            return -1;
        }
    
        return 0;
    });
      setData(response);
      console.log(response);
    }
  };
  fetchTeams();
    
  }, []);

  const Team : CSSProperties = {
    fontSize: "2em",
    // margin: "0 auto",
    height: "150%",
    width: "100%",
    transform: "translateY(25%)",
  }
  const TeamWinner : CSSProperties = {
    fontSize: "2em",
    height: "150%",
    width: "100%",
    // margin: "0 auto",
    // transform: "translateY(30%)",
  }
  const TeamUnknown : CSSProperties = {
    fontSize: "2em",
  }
  const Event : CSSProperties = {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    margin: "1em 0",
    overflow: "hidden",
    height: "4em",
    border: "1px solid #fff",
    // padding: "0.5em 0.5em",
    width: "100%",
    borderRadius: "5px",
    backgroundColor: "#ffffff0f",
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
        <h1 style={{flex:1}}>S'inscrire</h1>
        <a href="/connexion">connexion</a>
        <p>/</p>
        <a href="/inscription">inscription</a>
      </header>
      <div className={styles.page + " MatchList"} style={EventList}>
        {data.map((team, i) => (
          <div key={team.id} style={Event}>
            {team.team_home ? <span key={team.team_home.code} className={`fi fi-${team.team_home.code.toLowerCase()}`} style={team.team_home.id === team.winner ? TeamWinner : Team}></span> : <span className={"fi"} style={TeamUnknown}>?</span>}
            <span className="vs">VS</span>
            {team.team_away ? <span key={team.team_away.code} className={`fi fi-${team.team_away.code.toLowerCase()}`} style={team.team_away.id === team.winner ? TeamWinner : Team}></span> : <span className={"fi"} style={TeamUnknown}>?</span>}
          </div>
        ))}
        
      </div>
    </>
  );
}
