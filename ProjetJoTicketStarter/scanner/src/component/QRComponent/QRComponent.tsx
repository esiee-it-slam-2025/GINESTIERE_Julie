"use client"
const API_URL="localhost:5000/api/"
import React, { useEffect, useRef, useState } from 'react';
import QrScanner from 'qr-scanner';
import styles from './self.module.css';
import {GET as apiGET, POST as apiPOST} from "@/src/API/callAPI";



const QRScanner: React.FC<{event:number}> = ({event}:{event:number}) => {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [qrData, setQrData] = useState<string>("");
  const [validity, setValidity] = useState<string>("");
  const [scanning, setScanning] = useState<boolean>(true);

  useEffect(() => {
    if (!videoRef.current) return;

    const qrScanner = new QrScanner(videoRef.current, (result) => {
      setScanning(false);
      setQrData(result.data);
    }, {
      highlightScanRegion: false,
      highlightCodeOutline: false,
    });

    qrScanner.start();

    return () => {
      qrScanner.stop();
    };
  }, []);

  useEffect(() => {
    const checkQRCode = async ()=>{
      if (qrData) {
        setValidity("pending");
        var ticketCheckerValue = await apiPOST("checkTicket/",{
          'ticketId':qrData,
          'eventId':event,
        })
        console.log(ticketCheckerValue)
        setValidity(ticketCheckerValue.validity)
      }

    }
    checkQRCode()
  }, [qrData]);

  const handleScanAgain = () => {
    setScanning(true);
    setQrData("");
    setValidity("");
    
    // Re-initialize scanner
    if (videoRef.current) {
      const qrScanner = new QrScanner(videoRef.current, (result) => {
        setScanning(false);
        setQrData(result.data);
      }, {
        highlightScanRegion: false,
        highlightCodeOutline: false,
      });
      
      qrScanner.start();
    }
  };

  const getResultContainerClass = () => {
    if (!validity || validity === "pending") return styles.resultPending;
    if (validity === "valid") return styles.resultValid;
    return styles.resultInvalid;
  };

  const getResultTextClass = () => {
    if (!validity || validity === "pending") return styles.textPending;
    if (validity === "valid") return styles.textValid;
    return styles.textInvalid;
  };

  const getResultText = () => {
    if (validity === "pending") return "Vérification du billet...";
    if (validity === "valid") return "Billet valide ✓";
    if (validity === "invalid") return "Billet invalide ✗";
    if (validity === "used") return "Billet déjà utilisé ✗";
    if (validity === "wrong") return "Mauvais evenement ✗";
    if (validity === "error") return "Erreur de vérification";
    return "En attente de scan";
  };

  return (
    <div className={styles.scannerContainer}>
      <h1 className={styles.scannerTitle}>Scanner de Billets</h1>
      
      <div className={styles.videoContainer}>
        <video 
          ref={videoRef} 
          className={styles.scannerVideo} 
          playsInline
        />
        <div className={styles.scanOverlay}>
          <div className={styles.scanArea}>
            {scanning && <div className={styles.scanLine}></div>}
          </div>
        </div>
      </div>

      <div className={`${styles.resultContainer} ${getResultContainerClass()}`}>
        <div className={`${styles.resultText} ${getResultTextClass()}`}>
          {validity === "pending" && <span className={styles.spinner}></span>}
          {getResultText()}
        </div>
        {qrData && (
          <div className={styles.qrInfo}>
            ID: {qrData.substring(0, 20)}
            {qrData.length > 20 ? "..." : ""}
          </div>
        )}
        {!scanning && (
          <button 
            onClick={handleScanAgain}
            style={{
              marginTop: '1rem',
              padding: '0.5rem 1rem',
              backgroundColor: '#4299e1',
              color: 'white',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer',
              width: '100%',
              fontWeight: '500'
            }}
          >
            Scanner un autre billet
          </button>
        )}
      </div>
      
      {scanning && !qrData && (
        <p className={styles.scanInstructions}>
          Positionnez le code QR dans la zone de scan
        </p>
      )}
    </div>
  );
};

export default QRScanner;