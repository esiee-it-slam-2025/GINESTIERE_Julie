"use client"
import {GET as apiGET, POST as apiPOST} from '@/src/API/callAPI'
import { ChangeEvent, FormEvent, useEffect, useState } from 'react'
import { useRouter } from 'next/navigation';
import { LoginCredentials, LoginResponse } from '@/src/interfaces/auth';
import styles from './page.module.css'



export default function pages(){

    const [formData, setFormData] = useState({
        username: '',
        password: '',
      });
      const [error, setError] = useState<string>('');
      const [isLoading, setIsLoading] = useState<boolean>(false);
      const [session, setSession] = useState<boolean | undefined>(undefined)

      const router = useRouter();
    
      const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setFormData((prev) => ({
          ...prev,
          [name]: value,
        }));
      };


      const handleSubmit = async (e: FormEvent<HTMLFormElement>): Promise<void> => {
        e.preventDefault();
        setError('');
        setIsLoading(true);
    
        try {
          const apiResponse =  await apiPOST(
            'login/', 
            formData
          );
          
          // Handle successful login
          if(apiResponse.success){
            //   console.log('Login successful:', apiResponse);
            router.push("/")
            }else{
              console.log('Login unsuccessful:', apiResponse);
              setError(/*(apiResponse as LoginResponse).status +*/ 'Nom d\'utilisateur ou mot de passe incorect')
          }

          
          // Redirect user or update UI state
        //   router.push('/dashboard'); // Redirect to dashboard or appropriate page
        } catch (err) {
          console.error('Login error:', err);
          setError(err instanceof Error ? err.message : 'Login failed. Please try again.');
        } finally {
          setIsLoading(false);
        }
      };

      useEffect(()=>{
        const checkSession= async () => {
            const response = await apiGET("sessionCheck");
            console.log("Session Status",response)
            setSession(response.sessionValid)
            if(response.sessionValid){
              router.push("/")
            }
          }
          checkSession()
      },[])


    if(session == undefined){
        return<>
            <span>Loading ...</span>
        </>
    }
    if(session){
        return<><span>Connecté</span></>
    }

    return <>
    <div className={styles.formContainer}>
        <h1>Connexion</h1>
        {error && <span className={styles.serverErrorSpan}>{error}</span>}
        <form onSubmit={handleSubmit}>
            <div className={styles.formGroup}>
            <label htmlFor="username" className={styles.label}>Nom d'utilisateur</label>
            <input
                className={styles.input}
                type="text"
                id="username"
                name="username"
                value={formData.username}
                onChange={handleChange}
                required
                />
            </div>
            
            <div className={styles.formGroup}>
            <label htmlFor="password" className={styles.label}>Mot de passe</label>
            <input
                className={styles.input}
                type="password"
                id="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                required
                />
            </div>
            <input type="submit" value="Se connecter" disabled={isLoading} className={styles.submitButton}/>
        </form>
    </div>
    </>
}