import React from 'react';
import './cards.css';
import { Card } from '../card/card';
export const Cards= (props) => (
   <div className='cards'>
        {props.details.map(m=>(<Card key={m.id} m={m}></Card>))}
        ))
   </div>
);