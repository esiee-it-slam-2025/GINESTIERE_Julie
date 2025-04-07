"use client"
/***** CSS *****/
import styles from './page.module.css';
/***** ### *****/

/***** Modules *****/
import {GET as apiGET, POST as apiPOST} from '@/src/API/callAPI'
import { ChangeEvent, FormEvent, useEffect, useState } from 'react'
import { useRouter } from 'next/navigation';
/***** ####### *****/

interface localError  {
        email?: string,
        password?: string,
        password_confirm?: string,
        first_name?: string,
        last_name?: string,
}

export default function page(){



    const [formData, setFormData] = useState({
        email: '',
        password: '',
        password_confirm: '',
        first_name: '',
        last_name: '',
      });
      const [serverError, setServerError] = useState<string>('');
      const [localError, setLocalError] = useState<localError>({});
      const [isLoading, setIsLoading] = useState<boolean>(false);
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
        setServerError('');
        setLocalError({});
        setIsLoading(true);

        if(formData.password != formData.password_confirm){
            setLocalError((prev) => ({
                ...prev,
                password: "Les deux champs mot de passe doivent-être identique",
                password_confirm: "Les deux champs mot de passe doivent-être identique",
              }));
        }

        try {
            const apiResponse =  await apiPOST(
              'signIn/', 
              formData
            );

            if(apiResponse.success){
                //   console.log('Login successful:', apiResponse);
                router.push("/connexion")
                }else{
                  console.log('Login unsuccessful:', apiResponse);
                  setServerError(/*(apiResponse as LoginResponse).status +*/ apiResponse.error)
              }
        }catch(e){
            
        }


      }







    return<>
    <div className={styles.formContainer}>
        <h1>Inscription</h1>
        { 
            serverError && <span className={styles.serverErrorSpan}>{serverError}</span>
        }
        
      <form onSubmit={handleSubmit}>
        <div className={styles.formGroup}>
          <label className={styles.label} htmlFor="email">Mail</label>
          <input
            className={styles.input}
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />
          { 
            localError.email && <span className={styles.localErrorSpan}>{localError.email}</span>
          }
        </div>
        <div className={styles.formGroup}>
          <label className={styles.label} htmlFor="password">Mot de passe</label>
          <input
            className={styles.input}
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
          />
          { 
            localError.password && <span className={styles.localErrorSpan}>{localError.password}</span>
          }
        </div>
        <div className={styles.formGroup}>
          <label className={styles.label} htmlFor="password_confirm">Confirmer le mot de passe</label>
          <input
            className={styles.input}
            type="password"
            id="password_confirm"
            name="password_confirm"
            value={formData.password_confirm}
            onChange={handleChange}
          />
          { 
            localError.password_confirm && <span className={styles.localErrorSpan}>{localError.password_confirm}</span>
          }
        </div>
        <div className={styles.formGroup}>
          <label className={styles.label} htmlFor="first_name">Prénom</label>
          <input
            className={styles.input}
            type="text"
            id="first_name"
            name="first_name"
            value={formData.first_name}
            onChange={handleChange}
          />
          { 
            localError.first_name && <span className={styles.localErrorSpan}>{localError.first_name}</span>
          }
        </div>
        <div className={styles.formGroup}>
          <label className={styles.label} htmlFor="last_name">Nom</label>
          <input
            className={styles.input}
            type="text"
            id="last_name"
            name="last_name"
            value={formData.last_name}
            onChange={handleChange}
          />
          { 
            localError.last_name && <span className={styles.localErrorSpan}>{localError.last_name}</span>
          }
        </div>
        <input className={styles.submitButton} type="submit" value="S'inscrire"/>
      </form>
    </div>
    </>
}