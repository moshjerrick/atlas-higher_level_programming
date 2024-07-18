#!/usr/bin/node
function printBasedOnArguments(...args) {
    switch (args.length) {
        case 0:
            console.log('No argument');
            break;
        case 1:
            console.log('Argument found');
            break;
        case 2:
            console.log('Arguments found');
            break;
    }
}
