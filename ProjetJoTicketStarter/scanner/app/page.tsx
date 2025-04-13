"use client"
import {GET as apiGET, POST as apiPOST} from "@/src/API/callAPI";
import React, { useState, useEffect } from "react";
import { parseEvents } from "@/src/API/parseAPI";
import { Event } from "@/src/interfaces/events";
import Link from 'next/link';
import styles from './QRScanPage.module.css';

const QRScanPage: React.FC = () => {
  const [data, setData] = useState<Event[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        setIsLoading(true);
        const response = await apiGET("events");
        const eventList: Event[] = parseEvents({apiOutput: response})
        
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
        }
      } catch (error) {
        console.error("Error fetching events:", error);
      } finally {
        setIsLoading(false);
      }
    };
    
    fetchTeams();
  }, []);

  // Helper function to check if an event is today
  const isToday = (date: Date): boolean => {
    const today = new Date();
    return date.getDate() === today.getDate() &&
           date.getMonth() === today.getMonth() &&
           date.getFullYear() === today.getFullYear();
  }

  // Helper function to check if an event is in the past
  const isPast = (date: Date): boolean => {
    const now = new Date();
    return date < now;
  }

  // Helper function to format date
  const formatDate = (date: Date): string => {
    const day = date.getDate().toString().padStart(2, '0');
    // getMonth() is zero-based, so add 1
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const year = date.getFullYear();
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    
    return `${day}/${month}/${year} à ${hours}h${minutes}`;
  }

  // Get event card class based on date
  const getEventCardClass = (eventDate: Date): string => {
    if (isToday(eventDate)) {
      return `${styles.eventCard} ${styles.todayEvent}`;
    } else if (isPast(eventDate)) {
      return `${styles.eventCard} ${styles.pastEvent}`;
    }
    return styles.eventCard;
  }

  return (
    <div className={styles.container}>
      <h1 className={styles.pageTitle}>Sélectionner un événement</h1>
      
      {isLoading ? (
        <div className={styles.loadingContainer}>
          <div className={styles.loadingSpinner}></div>
        </div>
      ) : data.length === 0 ? (
        <div className={styles.noEvents}>
          Aucun événement disponible
        </div>
      ) : (
        <div className={styles.eventList}>
          {data.map((event) => {
            const eventDate = new Date(event.start);
            
            return (
              <Link 
                href={`./event?id=${event.id}`} 
                key={event.id} 
                className={getEventCardClass(eventDate)}
              >
                <div className={styles.eventHeader}>
                  <div>
                    <div className={styles.stadiumName}>
                      {event.stadium.name}
                    </div>
                    <div className={styles.eventTime}>
                      {formatDate(eventDate)}
                    </div>
                  </div>
                  <span className={styles.dateBadge}>
                    {isPast(eventDate) ? 'Passé' : isToday(eventDate) ? "Aujourd'hui" : 'À venir'}
                  </span>
                </div>
                
                {event.team_home && event.team_away && (
                  <div className={styles.matchInfo}>
                    {event.team_home.name} vs {event.team_away.name}
                  </div>
                )}
              </Link>
            );
          })}
        </div>
      )}
    </div>
  );
};

export default QRScanPage;