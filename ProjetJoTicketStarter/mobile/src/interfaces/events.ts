import { Stadium } from "./stadiums";
import { Team } from "./teams";
export interface Event {
    id: number;
    score: string;
    start: Date;
    team_away?: Team;
    team_home?: Team;
    winner?: number;
    stadium: Stadium;
}