import { Event } from "../interfaces/events"
export function parseEvents({apiOutput}:{apiOutput: any[]}) : Event[]{
    apiOutput.map(
        val => ( {
            id: val.id,
            score: val.score,
            start: new Date(val.score),
            team_away: val.team_away,
            team_home: val.team_home,
            winner: val.winner,
            stadium: val.stadium
        })
    )

    return apiOutput as Event[]
}