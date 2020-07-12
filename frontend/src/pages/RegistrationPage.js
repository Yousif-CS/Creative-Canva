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
    Select, 
    makeStyles,
    TextField,
    Typography,
    FormControl,
    InputLabel,
    MenuItem,

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
        backgroundColor: theme.palette.primary.main,
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
    formControl: {
        margin: theme.spacing(1),
        minWidth: 120,
    },
}));


function RegistrationPage({setAuth, ...props}) {

    const [values, setValues] = React.useState({
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        phoneNumber: '',
        suburb: '',
        postCode: '',
        gender: '',

    });

    function handleSubmit(event) {
        event.preventDefault();

        if (!values.email || !values.password || !values.firstName ||
            !values.lastName || !values.phoneNumber || !values.suburb ||
            !values.postCode || !values.gender) return;

        axios.post(`/register`, { ...values })
            .then((response) => {
                console.log(response);
                const data = response.date;
                setAuth(data.token, data.u_id);
                props.history.push('/');
            })
            .catch((err) => {});
    }

    const handleChange = name => event => {
        setValues({ ...values, [name]: event.target.value});
    };

    function handleGenderChange(event){
        const newstate = this.values;
        newstate.gender = event.target.value;
        setValues(newstate);
    }

    const classes = useStyles();

    return (
        <Container component="main" maxWidth="sm">
            <Box boxShadow={3} className={classes.card}>
                <Fragment>
                    <div><Person/></div>
                    <div>
                        <Typography component="h1" variant="h5">
                            Register
                        </Typography>
                    </div>
                </Fragment>


                <form className={classes.form} noValidate onSubmit={handleSubmit}>
                    <TextField 
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="firstName"
                        label="FirstName"
                        name="firstName"
                        type="text"
                        autofocus
                        />

                    <TextField 
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="lastName"
                        label="LastName"
                        name="lastName"
                        type="text"
                        autoComplete="current-password"
                        />
                
                    <TextField 
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="email"
                        label="Email"
                        name="email"
                        type="text"
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
                    <FormControl className={classes.formControl}>
                        <InputLabel id ="genderLabel">Gender</InputLabel>
                        <Select
                            labelId="gender"
                            id="gender"
                            value={values.gender}
                            onChange={handleChange}
                        >
                            <MenuItem value={"male"}>Male</MenuItem>
                            <MenuItem value={"female"}>Female</MenuItem>
                            <MenuItem value={"other"}>Other</MenuItem>
                        </Select>

                    </FormControl>
                    <TextField 
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="phoneNumber"
                        label="PhoneNumber"
                        name="phoneNumber"
                        type="text"
                    />
                    <TextField 
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="suburb"
                        label="Suburb"
                        name="suburb"
                        type="text"
                    />
                    <TextField 
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="postCode"
                        label="PostCode"
                        name="postCode"
                        type="text"
                    />
                    <Button type="submit" fullWidth variant="contained" color="secondary">
                        Register
                    </Button>

                    <Link href="/login">{'Already have an account? Login'}</Link>
                </form>
            </Box>
        </Container>
);
}

export default RegistrationPage;