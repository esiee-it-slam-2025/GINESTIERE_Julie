"use client"
import dynamic from 'next/dynamic';
import { useSearchParams } from 'next/navigation'
// Dynamically import the QRScanner component to avoid server-side rendering issues
const QRScanner = dynamic(() => import('../../src/component/QRComponent/QRComponent'), { ssr: false });


const QRScanPage: React.FC = () => {
    const searchParams = useSearchParams()
 
  const id = Number(searchParams.get('id'))

    return id ? <>
        <QRScanner event={id}/>
    </> : <></>

}

export default QRScanPage