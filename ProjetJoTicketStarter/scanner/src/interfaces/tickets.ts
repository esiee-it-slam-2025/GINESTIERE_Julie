import { Event } from "./events";

export interface Ticket{
    uuid:string,
    category:string,
    event: Event,
}