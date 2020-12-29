# Run this script with source("ab-table.r")
# And copy the output in the table of "ab.psy"
# ==========================================================================
# Explanation of script:
# This r script creates a table with all conditions.
# It just combines all conditions in one big table.
# It is an easy way to create a table, but of course,
# you need to understand the language R.
# Even when you know R, this script might be a bit difficult to follow.


# First, set a variable containing the stimulus1/stimulus2 interval times
times=c(0,100,196,280,430,590,900)

# later, we can just multiply these times 

# this is a table of all 6 stimulus/stimulus combinations
# the top three include a target

# there are 3 symbols without an L (n1,n2,n3) and one with (t1).

stimuli= rbind( c("n1","t1"),
                c("n2","t1"),
                c("n3","t1"),
                c("n1","n2"),
                c("n1","n3"),
                c("n2","n3")  )

for ( j in 1:6 ) # and all stimulus/stimulus combinations
for( position1 in c( -200 , 200 )) # x position of first stimulus
for( position2 in c( -200 , 200 ))
for( i in times )  # go through all times
  {
    # response (1=yes 2=no)
    if ( j < 4 ) r=1 else r=2
    
    # each time exists twice, except 0
    trial=paste(i,paste(stimuli[j,],collapse=" "),position1,position2,r)
    cat(paste( "  ",trial," \"",trial,"\"",sep=""),"\n")

    # the -1 time just is one in which the stimulus order is reversed
    # of course, there should be no -0, and thus times=0 is excluded
    # from the swap
    if ( i != 0 )
    {
    # negative SOA are those when the target is presented FIRST
    trial=paste(i,paste(rev(stimuli[j,]),collapse=" "),position1,position2,r)
    trialx=paste(-i,paste(rev(stimuli[j,]),collapse=" "),position1,position2,r)
    cat(paste( "  ",trial," \"",trialx,"\"",sep=""),"\n")
    }
  }
   
