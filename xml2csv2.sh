
awk -F'[=>]' ' {
                for ( i = 1; i <= NF; i++ )
                {
                        if ( $i ~ /dateTime/ )
                        {
                                dT = $( i + 1 )
                                gsub (/\"[ ]+.*|\"/, X, dT)
                        }
                        if ( $i ~ /SOATransactionID/ )
                        {
                                SID = $( i + 1 )
                                gsub (/\">.*|\"/, X, SID)
                        }
                        if ( $i ~ /<xml:tariffCode/ )
                        {
                                tC = $( i + 1 )
                                gsub (/<.*/, X, tC)
                        }
                }
} END {
        print dT, SID, tC
} ' OFS=, xmlfile

