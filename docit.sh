#!/bin/bash
FILES="Event Model Controller"
TESTNAMES="mtest.py etest.py stest.py"
TESTDIR="tests"
DOCDIR="$TESTDIR/doc"
COVERAGEDIR="$TESTDIR/coverage"
SRCDIR="src"

#functions
function mkdir_s {
    [ ! -d "$1" ] && mkdir "$1"
}

function Clean {
    echo Cleaning $TESTDIR ...
    [ -d "$TESTDIR" ] && rm -rf $TESTDIR/*
    coverage3 erase
}

function Doc {
    echo Making up $DOCDIR...
    mkdir_s $DOCDIR/
    mkdir_s $DOCDIR/html
    touch $DOCDIR/doc.txt
    touch $DOCDIR/doc.log
    
    for i in ${FILES}; do
        pydoc3 src.$i >> $DOCDIR/doc.txt
        pydoc3 -w src.$i >> $DOCDIR/doc.log
    done
    mv *.html $DOCDIR/html
}

function Coverage {
    echo Making up $COVERAGEDIR...
    mkdir_s $COVERAGEDIR/
    mkdir_s $COVERAGEDIR/html
    local COUNTER=0
    touch $COVERAGEDIR/coverage.log
    
    coverage3 erase
    for i in ${TESTNAMES}; do
        coverage3 run -a $i >> $COVERAGEDIR/coverage.log
    done
    coverage3 report ${TESTNAMES} > tests/coverage/coverage.txt
    coverage3 html -d $COVERAGEDIR/html ${TESTNAMES} >> $COVERAGEDIR/coverage.log
}

function PEP8 {
    echo PEP8 report: $TESTDIR/pep8.txt
    touch $TESTDIR/pep8.txt
    pep8 *.py | tee $TESTDIR/pep8.txt
}

function Pyflakes {
    echo Pyflakes report: $TESTDIR/pep8.txt
    touch $TESTDIR/pyflakes.txt
    pyflakes *.py | tee $TESTDIR/pyflakes.txt
}

function Help {
    echo "~~ Available commands ~~"
    echo "Feel free to mix them as you like"
    echo "Everything logs to $TESTDIR"
    echo "help          : Prints this help"
    echo "clean         : Cleans test dir"
    echo "coverage      : Runs coverage3, creates .txt and .html report"
    echo "doc           : Runs pydoc, creates .txt and .html report"
    echo "pep8          : Runs pep8, creates .txt report"
    echo "pyflakes      : runs pyflakes, creates .txt report"
    echo "all           : Runs all above"
    echo "run           : Runs main program, creates .log"
}
#work 
mkdir_s "$TESTDIR"

#no args supplied
if [ $# -eq 0 ]; then
    Help
    exit
fi

#arg all supplied
for arg in $@; do
    if [ "$arg" = "all" ]; then
            Clean
            Coverage
            Doc
            PEP8
            Pyflakes
            exit
    fi   
done

#other args
for arg in $@; do
    if [ "$arg" = "clean" ]; then
        Clean
    elif [ "$arg" = "docs" ]; then
        Doc
    elif [ "$arg" = "coverage" ]; then
        Coverage
    elif [ "$arg" = "pep8" ]; then
        PEP8
    elif [ "$arg" = "pyflakes" ]; then
        Pyflakes
    elif [ "$arg" = "help" ]; then
        Help
    elif [ "$arg" = "run" ]; then
        python3 main.py | tee $TESTDIR/main.log
    else
        Help
    fi
done


