import React from 'react';
import './card.css';
export const Card= (props)=> (
    <div className='card-container'>
        <h2>id:{props.m.id}</h2>
        <h2>name:{props.m.names_of_quiz}</h2>
        <h2>desc:{props.m.description}</h2>
        <h2>n:{props.m.number_of_questions}</h2>
    </div>
);