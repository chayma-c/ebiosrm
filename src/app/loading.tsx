const Loadingpage = ()=>{
return(

    <div  className="wrapper absolute top-0 left-0 w-screen bg-black-200 h-screen flex items-center justify-center" >
        <div className="container rotate-45 w-24  grid grid-cols-3 gap-x-1 gap-y-1  ">
            { new Array(9).fill().map((arr,i)=>{
                return <div key={i}  className="box w-7 h-7 bg-[#65cdef]" >

                    
                </div>

            }) }
        </div>
    </div>
)
}

export default Loadingpage