import React from 'react'
import testjson from '../testjson.json'
type Lead =  {
  Address: string;
  Owner: string;
  Phone: string;
  Email: string;
  Link: string;
}
let leads: Lead[]= []
const parseJson = () => {
  leads = testjson.leads
}

export const Table = () => {
  parseJson() 
  let rows = [];
  let count = 1;
  for(let lead of leads){
    rows.push(
      <tr>
            <th>{count}</th>
            <td>{lead.Address}</td>
            <td>{lead.Owner}</td>
            <td>{lead.Phone}</td>
            <td>{lead.Email}</td>
            <td>{lead.Link}</td>
      </tr>
    )
    count++;
  }
  return(

    <div className="overflow-x-auto">
      <table className="table table-zebra w-full">
        <thead>
          <tr>
            <th></th>
            <th>Address</th>
            <th>Owner</th>
            <th>Phone</th>
            <th>Email</th>
            <th>Link to Case</th>
          </tr>
        </thead>
        <tbody>
          {rows}
        </tbody>
  </table>
</div>
    )
}
