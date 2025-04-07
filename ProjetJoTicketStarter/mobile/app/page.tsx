"use client"
//import Image from "next/image";
import styles from "./page.module.css";
import "@/node_modules/flag-icons/css/flag-icons.min.css";
// import fetch  from "node-fetch";
// import {Response} from "node-fetch";
import React, { useState, useEffect, ChangeEvent, FormEvent } from "react";
import { Event } from "@/src/interfaces/events";
import { parseEvents } from "@/src/API/parseAPI";
import {GET as apiGET, POST as apiPOST} from "@/src/API/callAPI";
import NumberInput from "@/src/component/NumberInput/NumberInput";
import { getCookie, setCookie } from "@/src/API/cookies";

interface FormData{
  silver:number,
  gold:number,
  platinium:number,
  eventId:number|undefined,
}

export default function Home(req:any) {
  const [data, setData] = useState<Event[]>([]);
  const [selectedEvent, selectEvent] = useState<Event | undefined>(undefined);
  const [session, setSession] = useState<boolean>(false)


  const [formData, setFormData] = useState<FormData>({
    silver: 0,
    gold: 0,
    platinium:0,
    eventId:undefined,
  });
  const [error, setError] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);



  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };
  const handleButtons = (name:"silver" | "gold" | "platinium", buttonAction:boolean) => {
    //const { name, value } = ;
    setFormData((prev) => ({
      ...prev,
      [name]: buttonAction ? prev[name] + 1 : Math.max(prev[name] - 1,0),
      
    }));
  };

  useEffect(()=>{
    setFormData({
      silver: 0,
      gold: 0,
      platinium:0,
      eventId: selectedEvent?.id,
    })
  },[selectedEvent])

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
    checkSession();

    if(!getCookie("cart")){
      setCookie(
        'cart',
        [],
        5
      )
    }

  }, []);

  function handleEventClick({event}:{event:Event}){
    if(selectedEvent == event){
      selectEvent(undefined)
    }else{
      selectEvent(event)
    }
  }

  const handleSubmit = async (e: FormEvent<HTMLFormElement>): Promise<void> => {
    e.preventDefault();
    setError('');
    setIsLoading(true);

    try {
      const apiResponse =  await apiPOST(
        'tickets/', 
        formData
      );
      
      // Handle successful login
      if(apiResponse.success){
        
        }else{
          console.log('Ticket génération error:', apiResponse);
          setError(/*(apiResponse as LoginResponse).status +*/ 'Erreur de création de billets')
      }

      selectEvent(undefined)
      // Redirect user or update UI state
    //   router.push('/dashboard'); // Redirect to dashboard or appropriate page
    } catch (err) {
      console.error('Ticket génération error:', err);
      setError(err instanceof Error ? err.message : 'Erreur de création de billets');
    } finally {
      setIsLoading(false);
    }
  };




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
              <form className={styles.ticketControls} onSubmit={handleSubmit}>
                <div className={styles.ticketType}>
                  <label htmlFor="silver" className={styles.ticketLabel}>Silver</label>
                  <button type="button" className={styles.ticketMinusPlusButton} onClick={() => {handleButtons("silver", false)}}>-</button>
                  <NumberInput id="silver" name="silver" className={styles.numberInput} onChange={handleChange} value={formData.silver.toString()}/>
                  <button type="button" className={styles.ticketMinusPlusButton} onClick={() => {handleButtons("silver", true)}}>+</button>
                </div>
                <div className={styles.ticketType}>
                  <label htmlFor="gold" className={styles.ticketLabel}>Gold</label>
                  <button type="button" className={styles.ticketMinusPlusButton} onClick={() => {handleButtons("gold", false)}}>-</button>
                  <NumberInput id="gold" name="gold" className={styles.numberInput} onChange={handleChange}value={formData.gold.toString()}/>
                  <button type="button" className={styles.ticketMinusPlusButton} onClick={() => {handleButtons("gold", true)}}>+</button>
                </div>
                <div className={styles.ticketType}>
                  <label htmlFor="platinium" className={styles.ticketLabel}>Platinium</label>
                  <button type="button" className={styles.ticketMinusPlusButton} onClick={() => {handleButtons("platinium", false)}}>-</button>
                  <NumberInput id="platinium" name="platinium" className={styles.numberInput} onChange={handleChange} value={formData.platinium.toString()}/>
                  <button type="button" className={styles.ticketMinusPlusButton} onClick={() => {handleButtons("platinium", true)}}>+</button>
                </div>
                <input 
                  className={styles.addToCartButton} 
                  type="submit" 
                  disabled={!session || isLoading}
                  value="Ajouter au panier"
                  />
                  
              </form>
            )}
          </div>
        ))}
      </div>
    </>
  );
}