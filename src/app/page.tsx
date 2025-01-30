"use client"
import { Disclosure, DisclosureButton, DisclosurePanel } from "@headlessui/react";
import { GiHamburgerMenu } from "react-icons/gi";
import { CgProfile } from "react-icons/cg";
import { FaRegComments } from "react-icons/fa";
import { BiMessageSquareDots } from "react-icons/bi";
import { useState } from "react";
import * as s from "./navbar.style"
function My_navbar () {
  const Menu =   [{name : "Virtual Dashboard" ,icon :FaRegComments} , {name : "Dashboard" ,icon :CgProfile}  ,{name : "Profile" ,icon :BiMessageSquareDots}  ,{name : "Comments" ,icon :CgProfile} ]
  const Menujsx  = Menu.map((menu)=>{
    return( <s.menuitem key = {menu.name}>
            <menu.icon className="text-2xl text-gray-600 group-hover:text-white " />
      <s.title>
      {menu.name}
      </s.title>
     

    </s.menuitem>)
  })
  return(
    <s.Maincontainer  >
         
          <s.MenuHandler>
          {Menujsx}
          </s.MenuHandler>
     
      </s.Maincontainer>
  )

}
export default function Home() {
const [Toggle,setToggle] = useState(true)
  return (
    <> 
    <s.Pager  >
      <s.container >
      <Disclosure as="nav">
      
      <DisclosureButton onClick={()=> setToggle(!Toggle)} >
              <GiHamburgerMenu className="block  h-6 w-6" />
            </DisclosureButton>
      </Disclosure>
      {Toggle && <My_navbar /> }
     
      </s.container>
      <s.body>
        
      </s.body>

    </s.Pager>
    
    </>
  );
}
