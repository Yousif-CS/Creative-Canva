import React, { Fragment } from 'react';
import axios from 'axios';
import {
    Avatar,
    Box,
    Button,
    Container,
    Grid,
    Link,
    List,
    ListItem,
    ListItemIcon,
    makeStyles,
    TextField,
    Typography
} from '@material-ui/core'

import {
    Contacts,
    Person,
    Lock, 
    LockOpen,
} from '@material-ui/icons'


const useStyles = makeStyles((theme) => ({
    '@global': {
      body: {
        backgroundColor: theme.palette.primary.dark,
      },
    },
    card: {
      backgroundColor: theme.palette.background.paper,
      marginTop: theme.spacing(8),
      padding: theme.spacing(8),
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      borderRadius: theme.shape.borderRadius,
    },


}));


function LoginPage({setAuth, ...props}) {
    function handleSubmit(event) {
        event.preventDefault();

        // get input
        const email = event.target[0].value;
        const password = event.target[2].value;

        if (!email || !password) return;

        axios.post(`/login`, { email, password })
            .then((response) => {
                console.log(response);
                const data = response.date;
                setAuth(data.token, data.u_id);
                props.history.push('/');
            })
            .catch((err) => {});
    }
    const classes = useStyles();

    return (
        <Container component="main" maxWidth="sm">
            <Box boxShadow={3} className={classes.card}>
                <Fragment>
                    <div><LockOpen/></div>
                    <div>
                        <Typography component="h1" variant="h5">
                            Login
                        </Typography>
                    </div>
                </Fragment>


                <form noValidate onSubmit={handleSubmit}>
                    <TextField 
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="email"
                        label="Email"
                        name="email"
                        type="text"
                        autofocus
                    />
                    <TextField 
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="password"
                        label="Password"
                        name="password"
                        type="text"
                        autoComplete="current-password"
                    />
                    <Button type="submit" fullWidth variant="contained" color="secondary">
                        Sign In
                    </Button>
                    <Link href="/register">{'Do not have an account? Register'}</Link>
                </form>
            </Box>
        </Container>
);
}

export default LoginPage;