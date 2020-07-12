import React, { Fragment } from 'react';
import axios from 'axios';

import Avatar from 'react-avatar-edit';

import {
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

import FaceIcon from '@material-ui/icons/Face';
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


function DescriptionPage({ ...props }) {

    const [values, setValues] = React.useState({
        image: null,
        description: ''
    });

    function handleSubmit(event) {
        event.preventDefault();

        if (!values.description || !values.image){
            return
        }

        axios.post(`/addInfo`, { ...values })
            .then((response) => {
                console.log(response);
                const data = response.date;
                props.history.push("/login")
            })
            .catch((err) => {});
    }

    function onFileLoad(file){
        const newstate = values;
        newstate.image = file
        setValues(newstate);
    }

    function onCrop(preview){
        const newstate = values;
        newstate.image = preview;
        setValues(newstate);
    }
    
    function onClose(){
        const newstate = values;
        newstate.image = null;
        setValues(newstate)
    }

    const classes = useStyles();

    return (
        <Container component="main" maxWidth="sm">
            <Box boxShadow={5} className={classes.card}>
                <FaceIcon/>
                <Typography component="h1" variant="h5">
                Upload Photo
                </Typography>
                <Avatar 
                    width={250}
                    height={250}
                    onCrop={onCrop}
                    onClose={onClose}
                    onFileLoad={onFileLoad}
                    src={values.image}
                />

                <form className={classes.form} noValidate onSubmit={handleSubmit}>
                    <Link to="/login">
                        <Button type="submit" fullWidth variant="contained" margin="normal" color="secondary">
                            Upload
                        </Button>
                    </Link>
                </form>
            </Box>
        </Container>
);
}

export default DescriptionPage;