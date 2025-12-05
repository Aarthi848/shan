       IDENTIFICATION DIVISION.
       PROGRAM-ID. WRONG-VALIDATION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  USER-AGE    PIC X(3).

       PROCEDURE DIVISION.
           MOVE "ABC" TO USER-AGE.

           IF USER-AGE > "0" AND USER-AGE < "120"
               DISPLAY "Age is valid."
           ELSE
               DISPLAY "Age is invalid."
           END-IF.

           STOP RUN.

