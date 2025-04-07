import React, { useEffect, useState } from "react";

interface NumberInputProps extends React.InputHTMLAttributes<HTMLInputElement> {}

const NumberInput: React.FC<NumberInputProps> = ({ className = "", value=0, ...props }) => {
  const [nValue, setValue] = useState<string >(value.toString());

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newValue = e.target.value.replace(/\D/g, ''); // Retirer tout ce qui n'est pas un chiffre
    setValue(newValue); // Mettre à jour l'état avec la valeur filtrée
};

  useEffect(()=>{
    setValue(value.toString())
  },[value])


  return (
    <input
      type="text"
      value={nValue}
      onInput={handleChange}
      className={`${className}`}
      {...props}
    />
  );
};

export default NumberInput;

